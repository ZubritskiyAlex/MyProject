import {ActionTypes} from "../constants/action-types";
export const setReviews = (reviews) => {
    return{
        type: ActionTypes.SET_REVIEWS,
        payload: reviews,
    };
};


export const selectedReview = (review) => {
    return{
        type: ActionTypes.SELECTED_REVIEW,
        payload: review,
    };
};

export const removeSelectedReview = () => {
    return{
        type: ActionTypes.REMOVE_SELECTED_REVIEW,
    };
};
 /////

export const AddReview = () => {
    return{
        type: ActionTypes.ADD_REVIEW,
    };
};