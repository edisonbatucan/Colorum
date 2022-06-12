import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import Link from '@material-ui/core/Link';
import Paper from '@material-ui/core/Paper';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import DeleteForeverIcon from '@material-ui/icons/DeleteForever';
import EditIcon from '@material-ui/icons/Edit';
import Button from '@material-ui/core/Button';

const useStyles = makeStyles((theme) => ({
	cardMedia: {
		paddingTop: '56.25%', // 16:9
	},
	link: {
		margin: theme.spacing(1, 1.5),
	},
	cardHeader: {
		backgroundColor:
			theme.palette.type === 'light'
				? theme.palette.grey[200]
				: theme.palette.grey[700],
	},
	postTitle: {
		fontSize: '16px',
		textAlign: 'left',
	},
	postText: {
		display: 'flex',
		justifyContent: 'left',
		alignItems: 'baseline',
		fontSize: '12px',
		textAlign: 'left',
		marginBottom: theme.spacing(2),
	},
}));

const Vehicles = (props) => {
	const { vehicles } = props;
	const classes = useStyles();
	if (!vehicles || vehicles.length === 0) return <p>Can not find any vehicles, sorry</p>;
	return (
		<React.Fragment>
			<Container maxWidth="md" component="main">
				<Paper className={classes.root}>
					<TableContainer className={classes.container}>
						<Table stickyHeader aria-label="sticky table">
							<TableHead>
								<TableRow>
									<TableCell align="center"><strong>Car Name</strong></TableCell>
									<TableCell align="center"><strong>Price</strong></TableCell>
									<TableCell align="center"><strong>No. of seats</strong></TableCell>
									<TableCell align="center"><strong>Wheel Size</strong></TableCell>
									<TableCell align="center"><strong>Car Type</strong></TableCell>
									<TableCell align="Center"><strong>Action</strong></TableCell>
								</TableRow>
							</TableHead>
							<TableBody>
								{vehicles.map((vehicle) => {
									return (
										<TableRow>
											<TableCell align="center">
												<Link
													color="textPrimary"
													href={'/vehicle/' + vehicle.id}
													className={classes.link}
												>
													{vehicle.car_name}
												</Link>
											</TableCell>
											<TableCell align="center">₱ {vehicle.price}</TableCell>
											<TableCell align="center">{vehicle.num_seats}</TableCell>
											<TableCell align="center">{vehicle.wheel_size}</TableCell>
											<TableCell align="center">{vehicle.car_type}</TableCell>
											<TableCell align="center">
												<Link
													color="textPrimary"
													href={'/admin/edit/' + vehicle.id}
													className={classes.link}
												>
													<EditIcon></EditIcon>
												</Link>
												<Link
													color="textPrimary"
													href={'/admin/delete/' + vehicle.id}
													className={classes.link}
												>
													<DeleteForeverIcon></DeleteForeverIcon>
												</Link>
											</TableCell>
										</TableRow>
									);
								})}
								<TableRow>
									<TableCell colSpan={6} align="right">
										<Button
											href={'/admin/create'}
											variant="contained"
											color="primary"
										>
											New Vehicle
										</Button>
									</TableCell>
								</TableRow>
							</TableBody>
						</Table>
					</TableContainer>
				</Paper>
			</Container>
		</React.Fragment>
	);
};
export default Vehicles;