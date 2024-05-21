import { Typography } from '@mui/material';
import { Box } from '@mui/system';
import DrawerAppBar from './NavigationBar';
import Footer from './BottomNavBar';
import VB12 from './VB12';

export default function TopPage() {
    return (
        <Box sx={{ bgcolor: "#f7f6f5", color: 'black' }}>
            <DrawerAppBar />
            <Typography variant="h1" align="center" sx={{ paddingTop: '20vh' }}>
                テスト
            </Typography>
            <VB12 />
            <Footer />
        </Box>
    );
}