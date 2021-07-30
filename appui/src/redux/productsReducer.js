import {CREATE_PRODUCT, FETCH_PRODUCTS} from "./types";

const initialState = {
    products: [],
    fetchedProducts: []
}

export const productsReducer = (state= initialState, action) => {
  switch (action.type){
      case CREATE_PRODUCT:
          return {...state, products: state.products.concat([action.payload]) }
      case FETCH_PRODUCTS:
          return {...state, fetchedProducts: action.payload}
      default: return state
  }
}