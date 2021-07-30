import {ADD_PRODUCT} from "../constants";


const PRODUCTS = [
    {
        id: 1,
        description: 'top wear',
        price: 2500,

    },
    {
        id: 2,
        description: 'Laptop',
        price: 150,
    }
];

const products = (state = PRODUCTS, {id, description, price, type}) => {
    switch (type){
        case 'ADD_PRODUCT':
            return [
                ...state, {
                id,
                description,
                price,
                }
            ];
        default:
            return state;
    }
}
export default products;