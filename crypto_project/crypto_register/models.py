from django.db import models



class Coin(models.Model):
    shitcoin = 'Shitcoin'
    pumpndump = 'Pump N dump'
    halscoin = "Hal's Coin"
    coordinatordown= 'Coordinator Required'
    madebetterbyblockstream ="Made Better By Blockstream"

    CategoryChoices =[ 
        (shitcoin, 'Shitcoin'),
        (pumpndump, 'Pump N dump'),
        (halscoin, "Hal's Coin"),
        (coordinatordown, 'Coordinator Required'),
        (madebetterbyblockstream, "Made Better By Blockstream"),
    ]
    
    coin_title = models.CharField(max_length=40)
    coin_cat = models.CharField(
        max_length=28,
        choices=CategoryChoices,
        default=shitcoin,
    )
    coin_desc = models.TextField()
   
   
    # order = models.IntegerField()
    # class Meta():
    #     ordering = ['order',]

###UNFINISHED M2M system below.

# class Coin(models.Model):
#     coin_title = models.ManyToManyField('Category') #creates intermediate join table 
#     coin_desc = models.TextField()

#     def __str__(self):
#         return self.coin_title

# class Category(models.Model):
#     coin_cat = models.CharField(max_length=12)

#     def __str__(self):
#         return self.coin_cat

#associate the two via id, containing_model_id, other_model_id


