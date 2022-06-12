import React, { useEffect, useState } from 'react';
import './App.css';
import Vehicles from './components/admin/vehicles';
import VehicleLoadingComponent from './components/vehicles/VehicleLoading';
import axiosInstance from './axios';

function Admin() {
	const VehicleLoading = VehicleLoadingComponent(Vehicles);
	const [appState, setAppState] = useState({
		loading: true,
		vehicles: null,
	});

	useEffect(() => {
		axiosInstance.get().then((res) => {
			const allVehicles = res.data;
			setAppState({ loading: false, vehicles: allVehicles });
			console.log(res.data);
		});
	}, [setAppState]);

	return (
		<div className="App">
			<h1>Latest Vehicles</h1>
			<VehicleLoading isLoading={appState.loading} vehicles={appState.vehicles} />
		</div>
	);
}
export default Admin;