const initialState =[


];

export default function products(state = initialState, action) {
    if (action.type === 'ADD_PRODUCT') {
            return [
                ...state,
                action.payload
            ];
    } else if (action.type ==='FETCH_PRODUCTS_SUCCESS'){
        return action.payload;
    }
    return state;
}