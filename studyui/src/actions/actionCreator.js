import {ADD_PRODUCT} from "../constants";

export default addProduct = (id, description,price) => ({
    type: 'ADD_PRODUCT',
    id,
    description,
    price,
});