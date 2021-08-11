import React, {useEffect} from "react";
import {useDispatch , useSelector} from "react-redux";
import ProductComponent from "./ProductComponent";
import axios from "axios";
import {setProducts} from "../redux/actions/productActions";

const ProductListing = () => {
    const products = useSelector((state)=> state);
    const dispatch = useDispatch();

    const fetchProducts = async () => {
        const response = await axios
            .get('http://127.0.0.1:8000/api/product/')
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