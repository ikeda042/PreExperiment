import { Box, Button } from '@mui/material';
import { Link } from 'react-router-dom';
import DrawerAppBar from './NavigationBar';
import Footer from './BottomNavBar';
import { Stack } from '@mui/material';
import GitHubIcon from '@mui/icons-material/GitHub';

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
                        fontSize: '18px',
                        '&:hover': {
                            bgcolor: 'black',
                        },
                        '&:active': {
                            bgcolor: 'black',
                        }
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
                        fontSize: '18px',
                        '&:hover': {
                            bgcolor: 'black',
                        },
                        '&:active': {
                            bgcolor: 'black',
                        }
                    }}
                >
                    グルコースの検量線を作成する
                </Button>
                <Button
                    variant="contained"
                    component={Link}
                    to="https://www.google.com"
                    sx={{
                        bgcolor: 'black',
                        color: 'white',
                        padding: '16px 24px',
                        fontSize: '18px',
                        '&:hover': {
                            bgcolor: 'black',
                        },
                        '&:active': {
                            bgcolor: 'black',
                        }
                    }}
                    startIcon={<GitHubIcon />}
                >
                    予備実験ページ
                </Button>
            </Stack>

            <Footer />
        </Box>
    );
}
