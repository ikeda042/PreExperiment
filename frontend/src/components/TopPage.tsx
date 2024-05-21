import { Box, Typography, Button } from '@mui/material';
import { Link } from 'react-router-dom';
import DrawerAppBar from './NavigationBar';
import Footer from './BottomNavBar';
import { Stack } from '@mui/material';

export default function TopPage() {
    return (
        <Box sx={{ bgcolor: "#f7f6f5", color: 'black', display: 'flex', flexDirection: 'column', minHeight: '100vh', justifyContent: 'center', alignItems: 'center' }}>
            <DrawerAppBar />

            <Stack spacing={2} direction="column" mt={20} mb={20}>
                <Button
                    variant="contained"
                    component={Link}
                    to="/vb12"
                    sx={{
                        bgcolor: 'black',
                        color: 'white',
                        padding: '16px 24px',
                        fontSize: '18px'
                    }}
                >
                    VB12の検量線を作成する
                </Button>
                <Button
                    variant="contained"
                    component={Link}
                    to="/vb12"
                    sx={{
                        bgcolor: 'black',
                        color: 'white',
                        padding: '16px 24px',
                        fontSize: '18px'
                    }}
                >
                    VB12の検量線を作成する
                </Button>
                <Button
                    variant="contained"
                    component={Link}
                    to="https://www.google.com"
                    sx={{
                        bgcolor: 'black',
                        color: 'white',
                        padding: '16px 24px',
                        fontSize: '18px'
                    }}
                >
                    VB12の検量線を作成する
                </Button>
            </Stack>


            <Footer />
        </Box>
    );
}