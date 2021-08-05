const initialState = {
    products: [
        {
            id:0,
            title: 'New product'
        }
    ],

};

export default (state=initialState, action) => {
    switch (action.type){
        case 'SET_PRODUCTS':
            return {
                ...state,
                products: action.payload
            };
        default:
            return state;
    }
};