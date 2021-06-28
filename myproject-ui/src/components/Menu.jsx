import { Menu } from 'semantic-ui-react';
import React from "react";

const MenuComponent = () => (
<Menu>
        <Menu.Item name='browse' onClick={this.handleItemClick}>
          Store
        </Menu.Item>

        <Menu.Menu position='right' onClick={this.handleItemClick}>
           <Menu.Item name='signup' onClick={this.handleItemClick}>
            Total: &nbsp <b>0</b> USD
           </Menu.Item>

          <Menu.Item name='help' onClick={this.handleItemClick}>
            Cart(<b>0</b>)
          </Menu.Item>
        </Menu.Menu>
      </Menu>
);

export default Menu;
