import React from "react";
import {Input, Menu} from "semantic-ui-react";

const Filter = ({setFilter, filterBy, searchQuery }) =>(
    <Menu secondary>

          <Menu.Item
          active={filterBy === 'all'}
          onClick={setFilter.bind(this, 'all')}>
            All</Menu.Item>

        <Menu.Item

          active={filterBy === 'popular'}
          onClick={setFilter.bind(this, 'popular')}
        >Popular</Menu.Item>

        <Menu.Item

          active={filterBy === 'price_high'}
          onClick={setFilter.bind(this, 'price_high')}
        >Price_high</Menu.Item>

      <Menu.Item

          active={filterBy === 'price_low'}
          onClick={setFilter.bind(this, 'price_low')}
        >Price_high</Menu.Item>

          <Menu.Item
          active={filterBy === 'shop'}
          onClick={setFilter.bind(this, 'shop')}
        >Store</Menu.Item>
    <Menu.Item>
        <Input icon='search' onChange={e => setSearchQuery(e.target.value) }
               value={searchQuery}
               placeholder='Enter query'/>
    </Menu.Item>
    </Menu>
);

export default Filter;