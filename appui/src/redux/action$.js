import {CREATE_PRODUCT} from "./types";

export function createProduct(product){
    return{
        type: CREATE_PRODUCT,
        payload: product
    }
}