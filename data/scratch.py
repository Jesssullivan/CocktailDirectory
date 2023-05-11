# drink_id is the key for a drink record: structure should
# look something like:
# drink_id: title, author, step[line1, line2, ...], form[form1, form2, ...], onmenu<bool>
demo_drinks = dict()

demo_drinks['astoria'] = {"title": "Astoria",
                          "Author": "Shed",
                          "step": ["2 dashes Orange Bitters",
                                   "1.5oz Gin",
                                   "0.75oz Dry Vermouth",
                                   "0.5oz Iced Water"],
                          "form": [{
                              "Small Rock Glass": "Small Spritz of Lemon on the Prince Cube",
                              "Nick and Nora Glass": "Small spritz of Lemon in the Glass"
                          }],
                          "onWeb": False
                          }

