import React from "react";
import { Menu, Popup, List, Button, Image } from "semantic-ui-react";

const CartComponent = ({ title, id, image, removeFromCart }) => (
  <List selection divided verticalAlign="middle">
    <List.Item>
      <List.Content floated="right">
        <Button onClick={removeFromCart.bind(this, id)} color="red">
          Delete
        </Button>
      </List.Content>
      <Image avatar src={image} />
      <List.Content>{title}</List.Content>
    </List.Item>
  </List>
);

const MenuComponent = ({ totalPrice, count, items }) => (
  <Menu>
    <Menu.Item name="browse">Store creator</Menu.Item>

    <Menu.Menu position="right">
      <Menu.Item name="signup">
        Total: &nbsp; <b>{totalPrice}</b>&nbsp;USD.
      </Menu.Item>

      <Popup
        trigger={
          <Menu.Item name="help">
            Cart (<b>{count}</b>)
          </Menu.Item>
        }
        content={items.map(product => (
          <CartComponent {...product} />
        ))}
        on="click"
        hideOnScroll
      />
    </Menu.Menu>
  </Menu>
);

export default MenuComponent;
