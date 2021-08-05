const initialState = {
    isLoading: false,
    items: null,
};

export default (state=initialState, action) => {
    switch (action.type){
        case 'SET_PRODUCTS':
            return {
                ...state,
                products: action.payload,
                isReady: true
            };

        case 'SET_IS_READY':
            return {
                ...state,
                isReady: action.payload
            } ;
            break;
        default:
            return state;
    }
};