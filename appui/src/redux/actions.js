import {CREATE_PRODUCT, FETCH_PRODUCTS} from "./types";

export function createProduct(product){
    return{
        type: CREATE_PRODUCT,
        payload: product
    }
}


export function fetchProducts() {
    return async dispatch => {
        const response = await fetch('')
        const json = await response.json()
        dispatch({
        type: FETCH_PRODUCTS,
        payload: json  })
    }
}