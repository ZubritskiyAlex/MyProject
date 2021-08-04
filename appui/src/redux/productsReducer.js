import {CREATE_PRODUCT} from "./types";

const initialState = {
    products: [],
    fetchedProducts: []
}

export const productsReducer = (state= initialState, action) => {
  switch (action.type) {
      case CREATE_PRODUCT:
          return {...state, products: [...state.products, action.payload]}

      default: return state
  }
}