import {combineReducers} from 'redux';
import {productReducer, selectedProductReducer} from "./reducers/productReducer";
import {shopReducer, selectedShopReducer} from "./reducers/shopReducer";
import userReducer from "./reducers/userReducer";
import loadingReducer from "./reducers/loadingReducer";


const rootReducer = combineReducers({
    allProducts: productReducer,
    allShops: shopReducer,
    product:selectedProductReducer,
    shop:selectedShopReducer,
    user: userReducer,
    loading: loadingReducer

});

export default rootReducer;