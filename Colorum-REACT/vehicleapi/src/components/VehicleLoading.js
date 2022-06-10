import React from 'react';

function VehicleLoading(Component) {
	return function VehicleLoadingComponent({ isLoading, ...props }) {
		
		return (
			<p style={{ fontSize: '25px' }}>
				We are waiting for the data to load!...
			</p>
		);
	};
}
export default VehicleLoading;