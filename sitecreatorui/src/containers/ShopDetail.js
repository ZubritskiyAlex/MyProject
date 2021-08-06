import React, { useEffect } from "react";
import axios from "axios";
import { useParams } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import {removeSelectedShop, selectedShop} from "../redux/actions/shopActions";
const ShopDetail = () => {
  const { shopId } = useParams();
  let shop = useSelector((state) => state.shop);
  const {title, owner, description } = shop;
  const dispatch = useDispatch();

  const fetchShopDetail = async (id) => {
    const response = await axios
      .get(`https://6107ceafd73c6400170d3616.mockapi.io/api/v1/Shops${id}`)
      .catch((err) => {
        console.log("Err: ", err);
      });
    dispatch(selectedShop(response.data));
  };

  useEffect(() => {
    if (shopId && shopId !== "") fetchShopDetail(shopId);
    return () => {
      dispatch(removeSelectedShop());
    };
  }, [shopId]);
  return (
    <div className="ui grid container">
      {Object.keys(shop).length === 0 ? (
        <div>...Loading</div>
      ) : (
        <div className="ui placeholder segment">
          <div className="ui two column stackable center aligned grid">
            <div className="ui vertical divider">AND</div>
            <div className="middle aligned row">

              <div className="column rp">
                <h1>{title}</h1>
                <h2>
                  <a className="ui teal tag label">${description}</a>
                </h2>
                <h3 className="ui brown block header">{owner}</h3>

                <div className="ui vertical animated button" tabIndex="0">
                  <div className="hidden content">
                  </div>
                  <div className="visible content">Back to products</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default ShopDetail;