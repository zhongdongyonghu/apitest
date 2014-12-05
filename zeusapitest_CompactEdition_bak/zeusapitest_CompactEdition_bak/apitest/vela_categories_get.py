
def vela_categories_get():

#  schema_DS_vela_categories_get={
#        "$schema": "http://json-schema.org/draft-04/schema#",
#        #"id": "http://jsonschema.net#",
#        "type": "object",
#        ###"additionalProperties": false,
#        "properties": {
#            "result": {
#                #"id": "http://jsonschema.net/result#",
#                "type": "string",
#                "default": "success",
#                ##"additionalProperties": false
#            },
#            "info": {
#                #"id": "http://jsonschema.net/info#",
#                "type": "object",
#                ##"additionalProperties": false,
#                "properties": {
#                    "item_cates": {
#                        #"id": "http://jsonschema.net/info/item_cates#",
#                        "type": "array",
#                        #"additionalProperties": false,
#                        "items": {
#                            #"id": "http://jsonschema.net/info/item_cates/0#",
#                            "type": "object",
#                            #"additionalProperties": false,
#                            "properties": {
#                                "count": {
#                                    #"id": "http://jsonschema.net/info/item_cates/0/count#",
#                                    "type": "integer",
#                                    "default": 37313,
#                                    #"additionalProperties": false
#                                },
#                                "item_img_shape": {
#                                    #"id": "http://jsonschema.net/info/item_cates/0/item_img_shape#",
#                                    "type": "string",
#                                    "default": "square",
#                                    #"additionalProperties": false
#                                },
#                                "cid": {
#                                    #"id": "http://jsonschema.net/info/item_cates/0/cid#",
#                                    "type": "string",
#                                    "default": "1180",
#                                    #"additionalProperties": false
#                                },
#                                "parent_cid": {
#                                    #"id": "http://jsonschema.net/info/item_cates/0/parent_cid#",
#                                    "type": "integer",
#                                    "default": 0,
#                                    #"additionalProperties": false
#                                },
#                                "category_url": {
#                                    #"id": "http://jsonschema.net/info/item_cates/0/category_url#",
#                                    "type": "string",
#                                    "default": "weddings-events",
#                                    #"additionalProperties": false
#                                },
#                                "is_parent": {
#                                    #"id": "http://jsonschema.net/info/item_cates/0/is_parent#",
#                                    "type": "boolean",
#                                    "default": true,
#                                    #"additionalProperties": false
#                                },
#                                "is_narrow": {
#                                    #"id": "http://jsonschema.net/info/item_cates/0/is_narrow#",
#                                    "type": "boolean",
#                                    "default": false,
#                                    #"additionalProperties": false
#                                },
#                                "is_flashsales": {
#                                    #"id": "http://jsonschema.net/info/item_cates/0/is_flashsales#",
#                                    "type": "boolean",
#                                    "default": false,
#                                    #"additionalProperties": false
#                                },
#                                "sort_order": {
#                                    #"id": "http://jsonschema.net/info/item_cates/0/sort_order#",
#                                    "type": "integer",
#                                    "default": 1,
#                                    #"additionalProperties": false
#                                },
#                                "template_id": {
#                                    #"id": "http://jsonschema.net/info/item_cates/0/template_id#",
#                                    "type": "string",
#                                    "default": "157",
#                                    #"additionalProperties": false
#                                },
#                                "category_name": {
#                                    #"id": "http://jsonschema.net/info/item_cates/0/category_name#",
#                                    "type": "string",
#                                    "default": "Weddings & Events",
#                                    #"additionalProperties": false
#                                },
#                                "category_icon": {
#                                    #"id": "http://jsonschema.net/info/item_cates/0/category_icon#",
#                                    "type": "string",
#                                    "default": "http://litbjscss.rightinthebox.com/resource_11b9349fd2d94b6e8739b2c0a0eae78f84910fc7_mapplitb/mobile/category_icon/wedding&dress_icon.png",
#                                    #"additionalProperties": false
#                                },
#                                "category_icons": {
#                                    #"id": "http://jsonschema.net/info/item_cates/0/category_icons#",
#                                    "type": "object",
#                                    #"additionalProperties": false,
#                                    "properties": {
#                                        "old_icon": {
#                                            #"id": "http://jsonschema.net/info/item_cates/0/category_icons/old_icon#",
#                                            "type": "object",
#                                            #"additionalProperties": false,
#                                            "properties": {
#                                                "icon": {
#                                                    #"id": "http://jsonschema.net/info/item_cates/0/category_icons/old_icon/icon#",
#                                                    "type": "string",
#                                                    "default": "http://litbjscss.rightinthebox.com/resource_11b9349fd2d94b6e8739b2c0a0eae78f84910fc7_mapplitb/mobile/category_icon/wedding&dress_icon.png",
#                                                    #"additionalProperties": false
#                                                }
#                                            },
#                                            "required": [
#                                                "icon"
#                                            ]
#                                        },
#                                        "stick_icon": {
#                                            #"id": "http://jsonschema.net/info/item_cates/0/category_icons/stick_icon#",
#                                            "type": "object",
#                                            #"additionalProperties": false,
#                                            "properties": {
#                                                "icon_2x": {
#                                                    #"id": "http://jsonschema.net/info/item_cates/0/category_icons/stick_icon/icon_2x#",
#                                                    "type": "string",
#                                                    "default": "http://litbjscss.rightinthebox.com/resource_11b9349fd2d94b6e8739b2c0a0eae78f84910fc7_mapplitb/mobile/app_resource/icons/lightintheboxV2/c1180_icon@2x.png",
#                                                    #"additionalProperties": false
#                                                },
#                                                "icon_active": {
#                                                    #"id": "http://jsonschema.net/info/item_cates/0/category_icons/stick_icon/icon_active#",
#                                                    "type": "string",
#                                                    "default": "http://litbjscss.rightinthebox.com/resource_11b9349fd2d94b6e8739b2c0a0eae78f84910fc7_mapplitb/mobile/app_resource/icons/lightintheboxV2/c1180_icon_active.png",
#                                                    #"additionalProperties": false
#                                                },
#                                                "icon_2x_active": {
#                                                    #"id": "http://jsonschema.net/info/item_cates/0/category_icons/stick_icon/icon_2x_active#",
#                                                    "type": "string",
#                                                    "default": "http://litbjscss.rightinthebox.com/resource_11b9349fd2d94b6e8739b2c0a0eae78f84910fc7_mapplitb/mobile/app_resource/icons/lightintheboxV2/c1180_icon_active@2x.png",
#                                                    #"additionalProperties": false
#                                                },
#                                                "icon": {
#                                                    #"id": "http://jsonschema.net/info/item_cates/0/category_icons/stick_icon/icon#",
#                                                    "type": "string",
#                                                    "default": "http://litbjscss.rightinthebox.com/resource_11b9349fd2d94b6e8739b2c0a0eae78f84910fc7_mapplitb/mobile/app_resource/icons/lightintheboxV2/c1180_icon.png",
#                                                    #"additionalProperties": false
#                                                }
#                                            },
#                                            "required": [
#                                                "icon_2x",
#                                                "icon_active",
#                                                "icon_2x_active",
#                                                "icon"
#                                            ]
#                                        }
#                                    },
#                                    "required": [
#                                        "old_icon",
#                                        "stick_icon"
#                                    ]
#                                },
#                                "category_images": {
#                                    #"id": "http://jsonschema.net/info/item_cates/0/category_images#",
#                                    "type": "object",
#                                    #"additionalProperties": false,
#                                    "properties": {
#                                        "small_img_h_url": {
#                                            #"id": "http://jsonschema.net/info/item_cates/0/category_images/small_img_h_url#",
#                                            "type": "string",
#                                            "default": "http://litbimg5.rightinthebox.com/images/wholesale/201306/seeallwe.jpg",
#                                            #"additionalProperties": false
#                                        },
#                                        "small_img_v_url": {
#                                            #"id": "http://jsonschema.net/info/item_cates/0/category_images/small_img_v_url#",
#                                            "type": "string",
#                                            "default": "http://litbimg5.rightinthebox.com/images/wholesale/201008/Weddingl1280733955.jpg",
#                                            #"additionalProperties": false
#                                        },
#                                        "big_img_h_url": {
#                                            #"id": "http://jsonschema.net/info/item_cates/0/category_images/big_img_h_url#",
#                                            "type": "string",
#                                            "default": "http://litbimg5.rightinthebox.com/images/wholesale/201403/we1180.jpg",
#                                            #"additionalProperties": false
#                                        },
#                                        "big_img_v_url": {
#                                            #"id": "http://jsonschema.net/info/item_cates/0/category_images/big_img_v_url#",
#                                            "type": "string",
#                                            "default": "http://litbimg5.rightinthebox.com/images/wholesale/201209/litb_48915_1.jpg",
#                                            #"additionalProperties": false
#                                        },
#                                        "banner_img_url": {
#                                            #"id": "http://jsonschema.net/info/item_cates/0/category_images/banner_img_url#",
#                                            "type": "string",
#                                            "default": "http://litbimg5.rightinthebox.com/images/wholesale/200904/11240881997.jpg",
#                                            #"additionalProperties": false
#                                        }
#                                    },
#                                    "required": [
#                                        "small_img_h_url",
#                                        "small_img_v_url",
#                                        "big_img_h_url",
#                                        "big_img_v_url",
#                                        "banner_img_url"
#                                    ]
#                                },
#                                "display_text": {
#                                    #"id": "http://jsonschema.net/info/item_cates/0/display_text#",
#                                    "type": "string",
#                                    "default": "Weddings & Events",
#                                    #"additionalProperties": false
#                                }
#                            },
#                            "required": [
#                                "count",
#                                "item_img_shape",
#                                "cid",
#                                "parent_cid",
#                                "category_url",
#                                "is_parent",
#                                "is_narrow",
#                                "is_flashsales",
#                                "sort_order",
#                                "template_id",
#                                "category_name",
#                                "category_icon",
#                                "category_icons",
#                                "category_images",
#                                "display_text"
#                            ]
#                        },
#                        "required": [
#                            "0"
#                        ]
#                    }
#                },
#                "required": [
#                    "item_cates"
#                ]
#            },
#            "code": {
#                #"id": "http://jsonschema.net/code#",
#                "type": "string",
#                "default": "1000000",
#                #"additionalProperties": false
#            },
#            "error_msg": {
#                #"id": "http://jsonschema.net/error_msg#",
#                "type": "array",
#                #"additionalProperties": false,
#                "items": {}
#            }
#        },
#        "required": [
#            "result",
#            "info",
#            "code",
#            "error_msg"
#        ]
#    }

    schema_DS_vela_categories_get= {
        "type":"object",
        #"$schema": "http://json-schema.org/draft-03/schema",
        ##"id": "http://jsonschema.net",
        ##"required":false,
        "properties":{
            "code": {
                "type":"string",#"number",---test
                #"id": "http://jsonschema.net/code",
                #"required":false
            },
            "error_msg": {
                "type":"array",
                #"id": "http://jsonschema.net/error_msg",
                #"required":false
            },
            "info": {
                "type":"object",
                #"id": "http://jsonschema.net/info",
                #"required":false,
                "properties":{
                    "item_cates": {
                        "type":"array",
                        #"id": "http://jsonschema.net/info/item_cates",
                        #"required":false,
                        "items":
                                {
                                "type":"object",
                                #"id": "http://jsonschema.net/info/item_cates/0",
                                #"required":false,
                                "properties":{
                                    "category_icon": {
                                        "type":"string",
                                        #"id": "http://jsonschema.net/info/item_cates/0/category_icon",
                                        #"required":false
                                    },
                                    "category_icons": {
                                        "type":"object",
                                        #"id": "http://jsonschema.net/info/item_cates/0/category_icons",
                                        #"required":false,
                                        "properties":{
                                            "old_icon": {
                                                "type":"object",
                                                #"id": "http://jsonschema.net/info/item_cates/0/category_icons/old_icon",
                                                #"required":false,
                                                "properties":{
                                                    "icon": {
                                                        "type":"string",
                                                        #"id": "http://jsonschema.net/info/item_cates/0/category_icons/old_icon/icon",
                                                        #"required":false
                                                    }
                                                }
                                            },
                                            "stick_icon": {
                                                "type":"object",
                                                #"id": "http://jsonschema.net/info/item_cates/0/category_icons/stick_icon",
                                                #"required":false,
                                                "properties":{
                                                    "icon_2x_active": {
                                                        "type":"string",
                                                        #"id": "http://jsonschema.net/info/item_cates/0/category_icons/stick_icon/icon_2x_active",
                                                        #"required":false
                                                    },
                                                    "icon_2x": {
                                                        "type":"string",
                                                        #"id": "http://jsonschema.net/info/item_cates/0/category_icons/stick_icon/icon_2x",
                                                        #"required":false
                                                    },
                                                    "icon_active": {
                                                        "type":"string",
                                                        #"id": "http://jsonschema.net/info/item_cates/0/category_icons/stick_icon/icon_active",
                                                        #"required":false
                                                    },
                                                    "icon": {
                                                        "type":"string",
                                                        #"id": "http://jsonschema.net/info/item_cates/0/category_icons/stick_icon/icon",
                                                        #"required":false
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "category_images": {
                                        "type":"object",
                                        #"id": "http://jsonschema.net/info/item_cates/0/category_images",
                                        #"required":false,
                                        "properties":{
                                            "banner_img_url": {
                                                "type":"string",
                                                #"id": "http://jsonschema.net/info/item_cates/0/category_images/banner_img_url",
                                                #"required":false
                                            },
                                            "big_img_h_url": {
                                                "type":"string",
                                                #"id": "http://jsonschema.net/info/item_cates/0/category_images/big_img_h_url",
                                                #"required":false
                                            },
                                            "big_img_v_url": {
                                                "type":"string",
                                                #"id": "http://jsonschema.net/info/item_cates/0/category_images/big_img_v_url",
                                                #"required":false
                                            },
                                            "small_img_h_url": {
                                                "type":"string",
                                                #"id": "http://jsonschema.net/info/item_cates/0/category_images/small_img_h_url",
                                                #"required":false
                                            },
                                            "small_img_v_url": {
                                                "type":"string",
                                                #"id": "http://jsonschema.net/info/item_cates/0/category_images/small_img_v_url",
                                                #"required":false
                                            }
                                        }
                                    },
                                    "category_name": {
                                        "type":"string",
                                        #"id": "http://jsonschema.net/info/item_cates/0/category_name",
                                        #"required":false
                                    },
                                    "category_url": {
                                        "type":"string",
                                        #"id": "http://jsonschema.net/info/item_cates/0/category_url",
                                        #"required":false
                                    },
                                    "cid": {
                                        "type":"string",
                                        #"id": "http://jsonschema.net/info/item_cates/0/cid",
                                        #"required":false
                                    },
                                    "count": {
                                        "type":"number",
                                        #"id": "http://jsonschema.net/info/item_cates/0/count",
                                        #"required":false
                                    },
                                    "display_text": {
                                        "type":"string",
                                        #"id": "http://jsonschema.net/info/item_cates/0/display_text",
                                        #"required":false
                                    },
                                    "is_flashsales": {
                                        "type":"boolean",
                                        #"id": "http://jsonschema.net/info/item_cates/0/is_flashsales",
                                        #"required":false
                                    },
                                    "is_narrow": {
                                        "type":"boolean",
                                        #"id": "http://jsonschema.net/info/item_cates/0/is_narrow",
                                        #"required":false
                                    },
                                    "is_parent": {
                                        "type":"boolean",
                                        #"id": "http://jsonschema.net/info/item_cates/0/is_parent",
                                        #"required":false
                                    },
                                    "item_img_shape": {
                                        "type":"string",
                                        #"id": "http://jsonschema.net/info/item_cates/0/item_img_shape",
                                        #"required":false
                                    },
                                    "parent_cid": {
                                        "type":"number",
                                        #"id": "http://jsonschema.net/info/item_cates/0/parent_cid",
                                        #"required":false
                                    },
                                    "sort_order": {
                                        "type":"number",
                                        #"id": "http://jsonschema.net/info/item_cates/0/sort_order",
                                        #"required":false
                                    },
                                    "template_id": {
                                        "type":"string",
                                        #"id": "http://jsonschema.net/info/item_cates/0/template_id",
                                        #"required":false
                                    }
                                }
                            }


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



    return schema_DS_vela_categories_get


print vela_categories_get()
