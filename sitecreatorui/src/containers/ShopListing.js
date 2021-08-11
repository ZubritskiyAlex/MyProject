import React, {useEffect} from "react";
import axios from 'axios'
import {useDispatch, useSelector} from "react-redux";
import ShopComponent from "./ShopComponent";
import {setShops} from "../redux/actions/shopActions";

const ShopListing= () => {
    const shops = useSelector((state)=> state);
    const dispatch = useDispatch()


    const fetchShops = async () => {
        const response = await axios
            .get("http://127.0.0.1:8000/api/configureStore/")
            .catch((err)=>{
                console.log("Err", err);
            });
        dispatch(setShops(response.data));
       };
        useEffect(() =>{
            fetchShops();
        }, []);

       console.log(shops);
       return (
        <div className="ui grid container">
            <ShopComponent/>
        </div>
    );
};

export default ShopListing;