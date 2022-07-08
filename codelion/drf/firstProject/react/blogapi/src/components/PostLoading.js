import React from "react";

export default function PostLoading(Component) {
    return function PostLoadingComponent( {isLoading, ...props }) {
        if (!isLoading) return <Component {...props} />;
        return (
            <p style={{ fontsize:'25px' }}>
                We are waiting for the data to load...!
            </p> 
        );
    };
}

