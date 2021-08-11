import {ActionTypes} from "../constants/action-types";

export const setShops = (shops) =>{
    return{
        type:ActionTypes.SET_SHOPS,
        payload: shops,
    };
};


export const selectedShop = (shop) => {
    return {
        type: ActionTypes.SELECTED_SHOP,
        payload: shop,
    };
};

export const removeSelectedShop = () => {
    return{
        type: ActionTypes.REMOVE_SELECTED_SHOP,
    };
};

export const AddShop = () => {
    return{
        type: ActionTypes.ADD_SHOP,
    };
};