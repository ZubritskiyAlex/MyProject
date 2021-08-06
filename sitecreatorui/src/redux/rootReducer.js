import {combineReducers} from 'redux';
import {productReducer, selectedProductReducer} from "./reducers/productReducer";
import {shopReducer, selectedShopReducer} from "./reducers/shopReducer";


export default combineReducers({
    allProducts: productReducer,
    allShops: shopReducer,
    product:selectedProductReducer,
    shop:selectedShopReducer
});