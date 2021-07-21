import React from "react";
import {Card, Image, Icon, Button} from "semantic-ui-react";

const ProductCard = product =>{
  const {title,shop,price, image,addToCart, addedCount} = product;
  return(
  <Card>
    <Image src={image} />
    <Card.Content>
      <Card.Header>
          {title}
      </Card.Header>
      <Card.Meta>
        <span className='date'>
            {shop}
      </span>
      </Card.Meta>
    </Card.Content>
    <Card.Content extra>
      <a>
          <Icon name ='USD'/>
          {price}
      </a>
    </Card.Content>
    <Button onClick={addToCart.bind(this, product)}>Add to card{addedCount > 0 && `(${addedCount})`}</Button>
  </Card>
);
};

export default ProductCard;