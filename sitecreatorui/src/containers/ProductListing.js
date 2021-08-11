import React, {useEffect} from "react";
import {useDispatch , useSelector} from "react-redux";
import ProductComponent from "./ProductComponent";
import axios from "axios";
import {setProducts} from "../redux/actions/productActions";
import {API_PRODUCT_LIST_URL} from "../url_data/urlData";

const ProductListing = () => {
    const products = useSelector((state)=> state);
    const dispatch = useDispatch();

    const fetchProducts = async () => {
        const response = await axios
            .get(API_PRODUCT_LIST_URL)
            .catch((err)=>{
                console.log("Err",err);
            });
        dispatch(setProducts(response.data));
    };

    useEffect(() => {
        fetchProducts();
    }, []);
    console.log(products);
    return(
        <div className="ui grid container">
            <ProductComponent/>
        </div>
    );
};

export default ProductListing;