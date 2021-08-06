import React from "react";
import { Link } from "react-router-dom";
import {useSelector} from "react-redux";

const ShopComponent = () => {
    const shops = useSelector((state) =>state.allShops.shops)
    const renderList = shops.map((shop)=>{
        const {id, title, description, owner} = shop;
        return(<div className="four column wide" key={id}>
            <Link to={`/shop/${id}`}>
            <div className="ui link cards">
                <div className="card">
                    <div className="content">
                        <div className="header">{title}</div>
                        <div className="meta price">{description}</div>
                        <div className="meta">{owner}</div>
                </div>
            </div>
        </div>
        </Link>
     </div>
   );
  });
  return <>{renderList}</>;
};

export default ShopComponent;