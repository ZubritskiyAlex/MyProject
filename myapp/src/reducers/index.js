import {combineReducers} from "redux";

import products from './products';
import shops from './shops';
import filterProducts from "./filterProducts";


export default combineReducers({
    products,
    shops,
    filterProducts
})