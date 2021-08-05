import React from "react";
import {Menu} from "semantic-ui-react";

const MenuComponent = () =>(
    <Menu>
        <Menu.Item name="browse">
            SiteCreator
        </Menu.Item>

        <Menu.Menu position="right">
            <Menu.Item name="signup">
                Total: &nbsp; <b>0</b>$
            </Menu.Item>

            <Menu.Item name="help">
                Cart: &nbsp;<b>0</b>$
            </Menu.Item>
        </Menu.Menu>
    </Menu>
);
export default MenuComponent;

