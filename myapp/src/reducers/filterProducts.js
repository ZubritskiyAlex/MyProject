const initialState ='';

export default function filterProducts(state = initialState, action){
    if (action.type ==='FIND_PRODUCT') {
        return action.payload;
    }
    return state;
}