import {combineReducers} from 'redux';
import {AddProductReducer, productReducer, selectedProductReducer} from "./reducers/productReducer";
import {shopReducer, selectedShopReducer, AddShopReducer} from "./reducers/shopReducer";
import userReducer from "./reducers/userReducer";
import loadingReducer from "./reducers/loadingReducer";


const rootReducer = combineReducers({
    allProducts: productReducer,
    allShops: shopReducer,
    product:selectedProductReducer,
    shop:selectedShopReducer,
    addShop:AddShopReducer,
    addProduct: AddProductReducer,
    user: userReducer,
    loading: loadingReducer

});

export default rootReducer;