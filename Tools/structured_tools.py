from pydantic import BaseModel, Field
from langchain_core.tools import StructuredTool

#First create the schema
class ProductInput(BaseModel):
    price: float = Field(description='Price for one product' )
    quantity: int = Field(description='Number of products')
    discount: float = Field(
        default=0,
        description='Discount Percentage'
    )


#create the function
def calculate_price(
    price: float,
    quantity: int,
    discount: float = 0
) -> float:

    total = price * quantity

    discount_amount = total * (discount / 100)

    return total - discount_amount

#Create the tool


price_tool = StructuredTool.from_function(
    func=calculate_price,
    name='calculate_price',\
    description='Calculate the total price after applying the discount',
    args_schema=ProductInput   
)


#Call the function

result = price_tool.invoke({
    'price': 100.0,
    'quantity': 10,
    'discount': 12
})

print(result)