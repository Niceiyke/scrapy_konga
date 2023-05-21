import psycopg2
from scrapy.exceptions import DropItem
from itemadapter import ItemAdapter


class ScrapyKongaPipeline:
    def process_item(self, item, spider):
        return item
    
class Remove_Duplicate_item_Pipeline:
    def __init__(self):
        self.names_seen =set()

    def process_item(self,item,spider):
        adapter = ItemAdapter(item)

        if adapter['name'] in self.names_seen:

            raise DropItem(f'Duplicate item {item!r} found')
        
        else:
            self.names_seen.add(adapter['name'])
            return item



class SavingToDbpostgres:
    def __init__(self):
        self.con = psycopg2.connect(
            database="postgresec2",
            user="postgresec2",
            password="postgresec2",
            host="3.23.130.169",
            port="5432",
        )

        self.cur = self.con.cursor()

        print("connected")


    def process_item(self,item,spider):
        try:
            self.cur.execute(""" insert into products_product (name,stock,category,image,product_url,discount_percent,original_price,discount_price) values (%s,%s,%s,%s,%s,%s,%s,%s) on conflict(name) do nothing""",
                            (item['name'],item['stock'],item['category'],item['image'],item['url'],item['discount_percent'],item['original_price'],item['discount_price'],))
            #print(item)
            self.con.commit()

        except Exception as e:
            print('db_err',e)
            
 
        return item
  

