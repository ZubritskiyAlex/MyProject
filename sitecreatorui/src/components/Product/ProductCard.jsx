import React from 'react'
import {Card} from 'semantic-ui-react'

const ProductCard = ({title, description, price}) => (
    <Card>
    <Card.Content>
        <Card.Header>
            {title}
        </Card.Header>
        <Card.Meta>
            <span className='date'>
                {description}
            </span>
        </Card.Meta>
    </Card.Content>
    <Card.Content extra>
        <a>
            {price}
        </a>
    </Card.Content>
    </Card>
);

export default ProductCard;