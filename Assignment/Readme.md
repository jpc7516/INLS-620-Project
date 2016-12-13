#INLS-620 Online Grocery Service

__Jeffrey Chen__

__Machine-readable access through HTML+Microdata.__

_Could not get the DELETE method to work, tried PATCH, which didn't work either. I am not good at javascript..._

##Class Attributes:

title
* Contains the name of the page.

subtitle
* Contains the subtitle of the page.
    
category
* Describes a category of items for sale.
    
item
* Describes an individual item for sale.

ordered-item 
* Describes an individual item in the order form. Contains a link to the matching item for sale.
    
picture
* May appear in an item. Contains an image of the item.

description
* May appear in an item. Contains a description of the item.

add-item
* Used to describe a form for adding an item.

quantity
* Describes the number of items.

add
* Used to describe a form input that designates the adding of an item.

remove-item
* Used to describe a form for removing an item.

remove
* Used to describe a form input that designates the removal of an item.

price 
* Describes the price of an item or items (depending on quantity).

total_price
* Describes the total prices of all ordered items.


##Link Relations:

collection (from official registry)
* Target resource represents the collection resource for the context resource (an item).

payment (from official registry)
* Indicates a resource where payment is accepted.

order
* Indicates a resource where an order (ie: purchase order) of items is stored and updated.

item (from official registry)
* Indicates a resource that describes a particular item in the collection.

item_ref
* Indicates a resource that is the item of reference for an order form item
    
##Microdata Types:

https://schema.org/Service
* Denotes a provided service (e.g. delivery).

https://schema.org/SomeProducts
* A placeholder for multiple similar products of the same kind.

https://schema.org/PriceSpecification
* A structured value representing a price or price range. 

https://schema.org/Product
* Any offered product, such as a grocery item.

https://schema.org/Offer
* Denotes an offer to sell an item, in this case a grocery item.

https://schema.org/PropertyValue
* A property-value pair, e.g. representing a feature of a product.

https://schema.org/Invoice
* A statement of the money due for goods or services

##Microdata Properties:

name
* The name of the general item

description
* A description of the general item

url
* The URL of the item

sameAs
* URL of a reference Web page that unambiguously indicates the item's identity.

category
* A category of the item.

offer  
* An offer to sell a product.

image
* An image of the item. 

priceCurrency
* The currency (in 3-letter ISO 4217 format) of the price or a price component, when attached to PriceSpecification and its subtypes.

price
* The offer price of a product, or of a price component when attached to PriceSpecification and its subtypes.

additionalProperty
* A property-value pair representing an additional characteristic of the entitity, like quantity. Expected value is PropertyValue.

minimumPaymentDue
* The minimum payment required at the time.

paymentMethod
* The method by which the payment will be made (e.g. credit card).

    



