import React from "react";
import { Link } from "react-router-dom";
import ShopCard from "./ShopCard";

const ShopList = (props) => {
  console.log(props);

  const deleteShopHandler = (id) =>{
    props.getShopId(id);
  };


  const renderShopList = props.shops.map((shop)=>{
    return(
        <ShopCard
            shop={shop}
            clickHandler={deleteShopHandler }
            key={shop.id}
        />
    );
  });
  return(
      <div class="main">
        <h2>
          Shop List
          <Link to="/createshop">
          <button className="ui button blue right">Add Shop!</button>
          </Link>
          </h2>

        <div className="ui celled list">
          {renderShopList}
        </div>
      </div>
  );
};
export default ShopList;