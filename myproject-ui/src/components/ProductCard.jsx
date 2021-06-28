import React from "react";
import {Card, Image, Icon} from "semantic-ui-react";

const ProductCard = ({title,price,image}) =>(
  <Card>
    <Image src={image} />
    <Card.Content>
      <Card.Header>
          {title}
      </Card.Header>
      <Card.Meta>
        <span className='date'>
            {price}
      </span>
      </Card.Meta>
    </Card.Content>
      <a>
          <Icon name ='USD'/>
          {price}
      </a>
  </Card>
);

export default ProductCard;