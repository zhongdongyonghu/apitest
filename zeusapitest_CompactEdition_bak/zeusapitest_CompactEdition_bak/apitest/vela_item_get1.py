
def vela_item_get():

    schema_DS_vela_item_get={
        "type":"object",
        #"$schema": "http://json-schema.org/draft-03/schema",
        "properties":{
            "code": {
                "type":"string",
                #"required":false
            },
            "error_msg": {
                "type":"array",
                #"required":false
            },
            "info": {
                "type":"object",
                #"required":false,
                "properties":{
                    "item": {
                        "type":"object",
                        #"required":false,
                        "properties":{
                            "auto_post": {
                                "type":"boolean",
                                #"required":false
                            },
                            "cate_show_imgs": {
                                "type":"object",
                                #"required":false,
                                "properties":{
                                    "gallery": {
                                        "type":"object",
                                        #"required":false,
                                        "properties":{
                                            "rectangle": {
                                                "type":"string",
                                                #"required":false
                                            },
                                            "square": {
                                                "type":"string",
                                                #"required":false
                                            }
                                        }
                                    },
                                    "grid": {
                                        "type":"object",
                                        #"required":false,
                                        "properties":{
                                            "rectangle": {
                                                "type":"string",
                                                #"required":false
                                            },
                                            "square": {
                                                "type":"string",
                                                #"required":false
                                            }
                                        }
                                    },
                                    "list": {
                                        "type":"object",
                                        #"required":false,
                                        "properties":{
                                            "rectangle": {
                                                "type":"string",
                                                #"required":false
                                            },
                                            "square": {
                                                "type":"string",
                                                #"required":false
                                            }
                                        }
                                    }
                                }
                            },
                            "cid": {
                                "type":"string",
                                #"id": "http://jsonschema.net/info/item/cid",
                                #"required":false
                            },
                            "currency": {
                                "type":"string",
                                #"id": "http://jsonschema.net/info/item/currency",
                                #"required":false
                            },
                            "desc_url": {
                                "type":"string",
                                #"id": "http://jsonschema.net/info/item/desc_url",
                                #"required":false
                            },
                            "detail_desc": {
                                "type":"string",
                                #"id": "http://jsonschema.net/info/item/detail_desc",
                                # "required":false
                            },
                            "discount": {
                                "type":"string",
                                #"id": "http://jsonschema.net/info/item/discount",
                                #"required":false
                            },
                            "display_id": {
                                "type":"string",
                                #"id": "http://jsonschema.net/info/item/display_id",
                                #"required":false
                            },
                            "display_text": {
                                "type":"string",
                                #"id": "http://jsonschema.net/info/item/display_text",
                                # "required":false
                            },
                            "distribute_unavailable_skus": {
                                "type":"array",
                                #"id": "http://jsonschema.net/info/item/distribute_unavailable_skus",
                                #"required":false,
                                "items":
                                        {
                                        "type":"array",
                                        #"id": "http://jsonschema.net/info/item/distribute_unavailable_skus/0",
                                        #"required":false
                                    }


                            },
                            "favorite_times": {
                                "type":"number",
                                #"id": "http://jsonschema.net/info/item/favorite_times",
                                #"required":false
                            },
                            "is_discount": {
                                "type":"boolean",
                                # "id": "http://jsonschema.net/info/item/is_discount",
                                # "required":false
                            },
                            "is_freeshipping": {
                                "type":"boolean",
                                #"id": "http://jsonschema.net/info/item/is_freeshipping",
                                # "required":false
                            },
                            "is_price_reduction": {
                                "type":"boolean",
                                "id": "http://jsonschema.net/info/item/is_price_reduction",
                                #"required":false
                            },
                            "is_promotions": {
                                "type":"boolean",
                                "id": "http://jsonschema.net/info/item/is_promotions",
                                #"required":false
                            },
                            "is_recommended": {
                                "type":"boolean",
                                "id": "http://jsonschema.net/info/item/is_recommended",
                                #"required":false
                            },
                            "is_sale": {
                                "type":"boolean",
                                "id": "http://jsonschema.net/info/item/is_sale",
                                # "required":false
                            },
                            "is_specials": {
                                "type":"boolean",
                                "id": "http://jsonschema.net/info/item/is_specials",
                                #"required":false
                            },
                            "is_virtual": {
                                "type":"boolean",
                                "id": "http://jsonschema.net/info/item/is_virtual",
                                # "required":false
                            },
                            "item_icon": {
                                "type":"null",
                                "id": "http://jsonschema.net/info/item/item_icon",
                                # "required":false
                            },
                            "item_icons": {
                                "type":"array",
                                "id": "http://jsonschema.net/info/item/item_icons",
                                #"required":false,
                                "items":
                                        {
                                        "type":"number",
                                        #"id": "http://jsonschema.net/info/item/item_icons/0",
                                        # "required":false
                                    }


                            },
                            "item_id": {
                                "type":"number",
                                #"id": "http://jsonschema.net/info/item/item_id",
                                #"required":false
                            },
                            "item_img_shape": {
                                "type":"string",
                                #"id": "http://jsonschema.net/info/item/item_img_shape",
                                # "required":false
                            },
                            "item_imgs_small": {
                                "type":"array",
                                #"id": "http://jsonschema.net/info/item/item_imgs_small",
                                #"required":false,
                                "items":
                                        {
                                        "type":"object",
                                        #"id": "http://jsonschema.net/info/item/item_imgs_small/0",
                                        #"required":false,
                                        "properties":{
                                            "img_id": {
                                                "type":"string",
                                                #"id": "http://jsonschema.net/info/item/item_imgs_small/0/img_id",
                                                # "required":false
                                            },
                                            "img_url": {
                                                "type":"string",
                                                ##"id": "http://jsonschema.net/info/item/item_imgs_small/0/img_url",
                                                #"required":false
                                            },
                                            "position": {
                                                "type":"number",
                                                # "id": "http://jsonschema.net/info/item/item_imgs_small/0/position",
                                                #"required":false
                                            }
                                        },
                                        "required":["img_id1"],
                                        }


                            },
                            "item_imgs": {
                                "type":"array",
                                #"id": "http://jsonschema.net/info/item/item_imgs",
                                #"required":false,
                                "items":
                                        {
                                        "type":"object",
                                        #"id": "http://jsonschema.net/info/item/item_imgs/0",
                                        # "required":false,
                                        "properties":{
                                            "img_id": {
                                                "type":"string",
                                                #"id": "http://jsonschema.net/info/item/item_imgs/0/img_id",
                                                #"required":false
                                            },
                                            "img_url": {
                                                "type":"string",
                                                # "id": "http://jsonschema.net/info/item/item_imgs/0/img_url",
                                                # "required":false
                                            },
                                            "position": {
                                                "type":"number",
                                                # "id": "http://jsonschema.net/info/item/item_imgs/0/position",
                                                #"required":false
                                            }
                                        }
                                    }


                            },
                            "item_name": {
                                "type":"string",
                                #"id": "http://jsonschema.net/info/item/item_name",
                                #"required":false
                            },
                            "item_status": {
                                "type":"string",
                                # "id": "http://jsonschema.net/info/item/item_status",
                                #"required":false
                            },
                            "item_url": {
                                "type":"string",
                                #"id": "http://jsonschema.net/info/item/item_url",
                                # "required":false
                            },
                            "main_img_name": {
                                "type":"string",
                                #"id": "http://jsonschema.net/info/item/main_img_name",
                                # "required":false
                            },
                            "main_img_url": {
                                "type":"string",
                                #"id": "http://jsonschema.net/info/item/main_img_url",
                                #"required":false
                            },
                            "originalPrice": {
                                "type":"number",
                                # "id": "http://jsonschema.net/info/item/originalPrice",
                                #"required":false
                            },
                            "original_price": {
                                "type":"string",
                                # "id": "http://jsonschema.net/info/item/original_price",
                                #"required":false
                            },
                            "qty_min_unit": {
                                "type":"string",
                                # "id": "http://jsonschema.net/info/item/qty_min_unit",
                                # "required":false
                            },
                            "qty_order_max": {
                                "type":"number",
                                "id": "http://jsonschema.net/info/item/qty_order_max",
                                #"required":false
                            },
                            "qty_order_min": {
                                "type":"string",
                                #"id": "http://jsonschema.net/info/item/qty_order_min",
                                #"required":false
                            },
                            "review_count": {
                                "type":"number",
                                #"id": "http://jsonschema.net/info/item/review_count",
                                #"required":false
                            },
                            "review_rating": {
                                "type":"number",
                                #"id": "http://jsonschema.net/info/item/review_rating",
                                #"required":false
                            },
                            "sale_price": {
                                "type":"string",
                                #"id": "http://jsonschema.net/info/item/sale_price",
                                #"required":false
                            },
                            "sales_promotion_end_date": {
                                "type":"null",
                                #"id": "http://jsonschema.net/info/item/sales_promotion_end_date",
                                #"required":false
                            },
                            "sales_promotion_title": {
                                "type":"string",
                                #"id": "http://jsonschema.net/info/item/sales_promotion_title",
                                #"required":false
                            },
                            "sales_type": {
                                "type":"string",
                                #"id": "http://jsonschema.net/info/item/sales_type",
                                #"required":false
                            },
                            "save_price": {
                                "type":"string",
                                #"id": "http://jsonschema.net/info/item/save_price",
                                #"required":false
                            },
                            "short_desc": {
                                "type":"string",
                                #"id": "http://jsonschema.net/info/item/short_desc",
                                #"required":false
                            },
                            "sku_combinations": {
                                "type":"array",
                                #"id": "http://jsonschema.net/info/item/sku_combinations",
                                #"required":false
                            },
                            "skus": {
                                "type":"array",
                                #"id": "http://jsonschema.net/info/item/skus",
                                #"required":false
                            },
                            "stock_available_skus": {
                                "type":"array",
                                #"id": "http://jsonschema.net/info/item/stock_available_skus",
                                #"required":false
                            },
                            "stuff_status": {
                                "type":"string",
                                #"id": "http://jsonschema.net/info/item/stuff_status",
                                #"required":false
                            },
                            "template_id": {
                                "type":"string",
                                #"id": "http://jsonschema.net/info/item/template_id",
                                #"required":false
                            },
                            "thumbnail_img_url": {
                                "type":"string",
                                #"id": "http://jsonschema.net/info/item/thumbnail_img_url",
                                #"required":false
                            }
                        },
                        "required":["auto_post1"],
                        }
                }
            },
            "result": {
                "type":"string",
                #"id": "http://jsonschema.net/result",
                #"required":false
            }
        }
    }

    return schema_DS_vela_item_get


#print vela_item_get()
