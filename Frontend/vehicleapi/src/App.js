import React, { useEffect, useState } from "react";
import './App.css'
import Vehicle from './components/vehicles/Vehicle';
import VehicleLoadingComponent from './components/vehicles/VehicleLoading';
import axiosInstance from './axios';

function App() {
	const VehicleLoading = VehicleLoadingComponent(Vehicle);
	const [appState, setAppState] = useState({
		loading: false,
		vehicle: null,
	});

	useEffect(() => {
		axiosInstance.get().then((res) => {
			const allPosts = res.data;
			setAppState({ loading: false, vehicle: allPosts });
			console.log(res.data);
		});
	}, [setAppState]);
	return (
		<div className="App">
			<h1>Latest Vehicle</h1>
			<VehicleLoading isLoading={appState.loading} vehicle={appState.vehicle} />
		</div>
	);
}
export default App;