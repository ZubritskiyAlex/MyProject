import {ActionTypes} from "../constants/action-types";

const initialState = {
    shops: [
  //      {
  //      id: 1,
  //      title: "MiShop",
  //      description: "Welcome"
  //          },
  //      {
  //      id: 2,
  //      title: "APP STORE",
  //      description: "Welcome, whats up?"
  //          }
    ],
};

export const shopReducer = (state = initialState, {type, payload}) =>{
    switch (type){
        case ActionTypes.SET_SHOPS:
            return {...state, shops: payload};
        default:
            return state;
    }
};

export const selectedShopReducer = (state ={}, {type, payload}) =>{
    switch (type){
        case ActionTypes.SELECTED_SHOP:
            return {...state, ...payload};

        case ActionTypes.REMOVE_SELECTED_SHOP:
            return {...state, ...payload};
        default:
            return state;

    }
};


export const AddShopReducer = (state = initialState, {type, payload}) =>{
    switch (type){
        case ActionTypes.ADD_SHOP:
            return {...state, shops: payload};
        default:
            return state;
    }
};