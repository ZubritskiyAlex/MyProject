const initialState =[];

export default function products(state = initialState, action) {
    if (action.type === 'ADD_PRODUCT') {
            return [
                ...state,
                action.payload
            ];
    } else if (action.type ==='DELETE_PRODUCT'){
        return state;
    }
    return state;
}