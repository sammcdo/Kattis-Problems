<!DOCTYPE html>
<html class="theme_light" lang="en">
<head>
    <!-- Load sentry as early as possible -->
            <script nonce="8684f29263b1aaa88a2c1676a856e6dee4c493b2ceb6217157e3bc6d9bd9b610" src="https://js.sentry-cdn.com/1ad5e9767ad243d396a93ef40135e743.min.js" crossorigin="anonymous" data-lazy="no"></script>

    <script nonce="8684f29263b1aaa88a2c1676a856e6dee4c493b2ceb6217157e3bc6d9bd9b610" type="module">
        Sentry.onLoad(function() {
            Sentry.init({
                dsn: "https://1ad5e9767ad243d396a93ef40135e743:0f66eac85d88443baa349f5bc2497f28@sentry.io/271015",
                release: "beb17c29c8e61740de380510c2a02fa74a366903",
                environment: "edu",
                whitelistUrls: [
                    /https?:\/\/open\.kattis\.com/                 ],
                ignoreErrors: [
                    "Non-Error exception captured",                     "Non-Error promise rejection captured",                    'ResizeObserver loop limit exceeded'                ],
                ignoreUrls: ['/static\.cloudflareinsights\.com/'],                 autoSessionTracking: false,
                integrations: [                    new Sentry.BrowserTracing(),
                ],
                tracesSampleRate: 0,
                profilesSampleRate: 1.0,
                replaysSessionSampleRate: 0,                 replaysOnErrorSampleRate: 0,                 tracePropagationTargets: ["localhost", /https?:\/\/open\.kattis\.com/],             });
                        Sentry.setUser({
                username: "king-mcd",
                                email: "samcdowell2@liberty.edu",
                            })
                        Sentry.configureScope((scope) => scope.setTransactionName("submissions_src_file"));         })
    </script>

    <meta charset="UTF-8" >
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>404: Not Found &ndash; Kattis, Kattis</title>

    <!-- Jquery and Jquery-ui -->
    <link href="/assets/6ca8295fdd320959403ec48ee3c6cbbe/jquery-ui-dist/jquery-ui.theme.min.css" rel="stylesheet">
    <script nonce="8684f29263b1aaa88a2c1676a856e6dee4c493b2ceb6217157e3bc6d9bd9b610" src="/assets/6ca8295fdd320959403ec48ee3c6cbbe/jquery/dist/jquery.min.js"></script>
    <script nonce="8684f29263b1aaa88a2c1676a856e6dee4c493b2ceb6217157e3bc6d9bd9b610" src="/assets/6ca8295fdd320959403ec48ee3c6cbbe/jquery-ui-dist/jquery-ui.min.js"></script>

    <!-- Timezone Cookie -->
    <script nonce="8684f29263b1aaa88a2c1676a856e6dee4c493b2ceb6217157e3bc6d9bd9b610" type="module" src="/js/eb05e77fa1d149cc2f8b42eb9dbbfc98/modules/timezone.js"></script>

    <!-- Fonts/Icons -->
    <link href="/assets/6ca8295fdd320959403ec48ee3c6cbbe/@fortawesome/fontawesome-free/css/all.min.css" rel="stylesheet">

            <link href="/assets/6ca8295fdd320959403ec48ee3c6cbbe/@fontsource/merriweather/300.css" rel="stylesheet">
        <link href="/assets/6ca8295fdd320959403ec48ee3c6cbbe/@fontsource/merriweather/300-italic.css" rel="stylesheet">
            <link href="/assets/6ca8295fdd320959403ec48ee3c6cbbe/@fontsource/merriweather/400.css" rel="stylesheet">
        <link href="/assets/6ca8295fdd320959403ec48ee3c6cbbe/@fontsource/merriweather/400-italic.css" rel="stylesheet">
            <link href="/assets/6ca8295fdd320959403ec48ee3c6cbbe/@fontsource/merriweather/700.css" rel="stylesheet">
        <link href="/assets/6ca8295fdd320959403ec48ee3c6cbbe/@fontsource/merriweather/700-italic.css" rel="stylesheet">
                <link href="/assets/6ca8295fdd320959403ec48ee3c6cbbe/@fontsource/ubuntu/300.css" rel="stylesheet">
        <link href="/assets/6ca8295fdd320959403ec48ee3c6cbbe/@fontsource/ubuntu/300-italic.css" rel="stylesheet">
            <link href="/assets/6ca8295fdd320959403ec48ee3c6cbbe/@fontsource/ubuntu/400.css" rel="stylesheet">
        <link href="/assets/6ca8295fdd320959403ec48ee3c6cbbe/@fontsource/ubuntu/400-italic.css" rel="stylesheet">
            <link href="/assets/6ca8295fdd320959403ec48ee3c6cbbe/@fontsource/ubuntu/500.css" rel="stylesheet">
        <link href="/assets/6ca8295fdd320959403ec48ee3c6cbbe/@fontsource/ubuntu/500-italic.css" rel="stylesheet">
            <link href="/assets/6ca8295fdd320959403ec48ee3c6cbbe/@fontsource/ubuntu/700.css" rel="stylesheet">
        <link href="/assets/6ca8295fdd320959403ec48ee3c6cbbe/@fontsource/ubuntu/700-italic.css" rel="stylesheet">
    
    <!-- DateRangePicker CSS -->
    <link href="/assets/6ca8295fdd320959403ec48ee3c6cbbe/bootstrap-daterangepicker/daterangepicker.css" rel="stylesheet">

    <!-- Editable and Select2 -->
    <link href="/assets/6ca8295fdd320959403ec48ee3c6cbbe/select2/dist/css/select2.css" rel="stylesheet">

            <link rel="apple-touch-icon-precomposed" sizes="57x57"   href="/images/favicon/apple-touch-icon-57x57.png">
        <link rel="apple-touch-icon-precomposed" sizes="114x114" href="/images/favicon/apple-touch-icon-114x114.png">
        <link rel="apple-touch-icon-precomposed" sizes="72x72"   href="/images/favicon/apple-touch-icon-72x72.png">
        <link rel="apple-touch-icon-precomposed" sizes="144x144" href="/images/favicon/apple-touch-icon-144x144.png">
        <link rel="apple-touch-icon-precomposed" sizes="60x60"   href="/images/favicon/apple-touch-icon-60x60.png">
        <link rel="apple-touch-icon-precomposed" sizes="120x120" href="/images/favicon/apple-touch-icon-120x120.png">
        <link rel="apple-touch-icon-precomposed" sizes="76x76"   href="/images/favicon/apple-touch-icon-76x76.png">
        <link rel="apple-touch-icon-precomposed" sizes="152x152" href="/images/favicon/apple-touch-icon-152x152.png">
        <link rel="icon" type="image/png" href="/images/favicon/favicon-196x196.png" sizes="196x196">
        <link rel="icon" type="image/png" href="/images/favicon/favicon-96x96.png"   sizes="96x96">
        <link rel="icon" type="image/png" href="/images/favicon/favicon-32x32.png"   sizes="32x32">
        <link rel="icon" type="image/png" href="/images/favicon/favicon-16x16.png"   sizes="16x16">
        <link rel="icon" type="image/png" href="/images/favicon/favicon-128.png"     sizes="128x128">
        <link rel="shortcut icon"         href="/images/favicon/favicon.ico">
        <meta name="application-name"                content="Kattis, Kattis">
        <meta name="msapplication-TileColor"         content="#FFFFFF">
        <meta name="msapplication-TileImage"         content="/images/favicon/mstile-144x144.png">
        <meta name="msapplication-square70x70logo"   content="/images/favicon/mstile-70x70.png">
        <meta name="msapplication-square150x150logo" content="/images/favicon/mstile-150x150.png">
        <meta name="msapplication-wide310x150logo"   content="/images/favicon/mstile-310x150.png">
        <meta name="msapplication-square310x310logo" content="/images/favicon/mstile-310x310.png">
    
    <!-- Own CSS -->
    <link rel="stylesheet" href="/css/c9afd42202d23ecd54f16420b3da1b38/style.css">
    <style type="text/css">           .logo {
         background-color: ;
     }
          :root {
                      --branding-border: linear-gradient(rgb(240,176,52), rgb(240,176,52));
              }

          div.page-content.clearfix.above-everything.alert.alert-danger { color: #31708f; background: #d9edf7; border-color: #bce8f1; }
div.page-content.clearfix.above-everything.alert.alert-danger div.main-content { padding-bottom: 0; }

         </style>

    <script nonce="8684f29263b1aaa88a2c1676a856e6dee4c493b2ceb6217157e3bc6d9bd9b610" type="text/javascript">
        window.page_loaded_at = new Date();
        jQuery.noConflict();
    </script>

    
</head>

<body class=" l-body_grid"  >





<header class="l-page_header">
    <div class="page_header-arrow_expand_collapse">
        <i class="page_header-arrow_expand_collapse-arrow"></i>
    </div>
    <div class="page_header-wrapper">
        <div class="logo-container">
            <a class="logo-link" href="/" title="Kattis">
                <img class="logo" src="/images/site-logo?v=0a3f6018aacf449381741e45cf0ff6ba" alt="Kattis logo" />
            </a>
            <h4 class="logo-container-text">Kattis</h4>
            <button class="menu_mobile_link" >
                <i class="fas fa-bars menu_mobile_link_icon"></i>
            </button>
            <script nonce="8684f29263b1aaa88a2c1676a856e6dee4c493b2ceb6217157e3bc6d9bd9b610" type="module" src="/js/eb05e77fa1d149cc2f8b42eb9dbbfc98/pages/master/nav.js"></script>
        </div>
        <div class="branding_border"></div>
        <div class="page_header-content">
            <nav>
                <ul class="main_menu">
                                                                    <li>
                            <a  href="/problems" class="main_menu-item main_menu-item_link  " title="Problems">
                                                                    <i class="fas fa-puzzle-piece main_menu-item_icon"></i>
                                                                <span class="main_menu-item_name ">Problems</span>
                                                            </a>
                        </li>
                                                                    <li>
                            <a  href="/contests" class="main_menu-item main_menu-item_link  " title="Contests">
                                                                    <i class="fas fa-award main_menu-item_icon"></i>
                                                                <span class="main_menu-item_name ">Contests</span>
                                                            </a>
                        </li>
                                                                    <li>
                            <a  href="/challenge" class="main_menu-item main_menu-item_link  " title="Challenge">
                                                                    <i class="fas fa-star main_menu-item_icon"></i>
                                                                <span class="main_menu-item_name beta_label">Challenge</span>
                                                            </a>
                        </li>
                                                                    <li>
                            <a  href="/ranklist" class="main_menu-item main_menu-item_link  " title="Ranklists">
                                                                    <i class="fas fa-trophy main_menu-item_icon"></i>
                                                                <span class="main_menu-item_name ">Ranklists</span>
                                                            </a>
                        </li>
                                                                    <li>
                            <a  href="/jobs" class="main_menu-item main_menu-item_link  " title="Jobs">
                                                                    <i class="fas fa-suitcase main_menu-item_icon"></i>
                                                                <span class="main_menu-item_name ">Jobs</span>
                                                            </a>
                        </li>
                                                                    <li>
                            <a  href="/languages" class="main_menu-item main_menu-item_link  " title="Languages">
                                                                    <i class="fas fa-code main_menu-item_icon"></i>
                                                                <span class="main_menu-item_name ">Languages</span>
                                                            </a>
                        </li>
                                                                    <li>
                            <a  href="/info" class="main_menu-item main_menu-item_link  " title="Info">
                                                                    <i class="fas fa-info main_menu-item_icon"></i>
                                                                <span class="main_menu-item_name ">Info</span>
                                                            </a>
                        </li>
                                                                    <li>
                            <a  href="https://support.kattis.com" class="main_menu-item main_menu-item_link  " title="Help">
                                                                    <i class="fas fa-question main_menu-item_icon"></i>
                                                                <span class="main_menu-item_name ">Help</span>
                                                            </a>
                        </li>
                                    </ul>
            </nav>
                            <div class="header_item_margin search-lower">
                    <label for="search_input" class="search-label search-label-right">Search</label>
                    <form id="search_form" method="GET" action="/search" class="search">
                                                    <img src="/images/site/header/logo-empty.png?0bb770=" alt="Kattis Cat" class="search-mascot" />
                                                <input id="search_input" type="search" name="q" class="search-input" placeholder="Search Kattis" />
                        <i id="search_submit" class="fas fa-search search-icon"></i>
                    </form>
                </div>
            
        </div>
    </div>
</header>

<script nonce="8684f29263b1aaa88a2c1676a856e6dee4c493b2ceb6217157e3bc6d9bd9b610" type="text/javascript">
    jQuery(function($) {
        $('.page_header-arrow_expand_collapse').click(function() {
            $('body').toggleClass('header-collapsed');
        });
    });
</script>

<div class="l-main_area">
    

    
    <main class="flex flex-col grow content_padding">
        



<div class="top_bar ">
    <script nonce="8684f29263b1aaa88a2c1676a856e6dee4c493b2ceb6217157e3bc6d9bd9b610" type="module" src="/js/eb05e77fa1d149cc2f8b42eb9dbbfc98/pages/master/top_bar.js"></script>
    <div class="branding_border"></div>
            <div class="top_bar-content-wrapper">
            <div class="top_bar-section top_bar-section-large">
                <div class="breadcrumb top_bar-item">
                                                            <span class="breadcrumb-current">
                                                    404: Not Found
                                            </span>
                </div>

                            </div>

            <div class="top_bar-section tooltip-right-container top_bar-section-small">

                
                

                                                            <div class="top_bar-item top_bar-item-right top_bar-item-button top_bar-item-button-user">
                            <div class="top_bar-button">

                                <a class="whitespace-nowrap" href="/supporter">
                                                                            Support Kattis                                                                    </a>

                            </div>
                        </div>
                                        <div class="top_bar-item top_bar-item-right top_bar-item-button top_bar-item-button-user">
                        <!-- Tooltip -->
                        <div class="tooltip-container">
                            <div class="top_bar-button whitespace-nowrap" data-openTooltipId="top_user_tooltip" data-tooltipType="right" data-tooltipUseBackground="true">Samuel McDowell<i class="fas fa-chevron-down top_bar-button-chevron_down"></i><i class="fas fa-chevron-up top_bar-button-chevron_up"></i></div>
                            <div id="top_user_tooltip" class="tooltip">
                                <span class="tooltip-arrow"></span>
                                <div class="tooltip-content tooltip-menu tooltip-top_bar">
                                    <i class="fas fa-times tooltip-close tooltip-top_bar-close"></i>
                                    <a href="/users/king-mcd" class="image_info static_link"><div class="image_info-image-container"><img src="/images/users/king-mcd?v=299a66dd77ad47a37d4710afa74b1aa4"alt="Samuel McDowell"class="image_info-image image_info-image-strip image_info-image-rounded ""/></div><div class="image_info-text-container"><span class="image_info-text-main image_info-text-main-user">Samuel McDowell</span><span class="image_info-text-sub"><ul class="image_info-list-sub"><li>Score: 729.6</li><li>Rank: 990</li></ul></span></div></a>
                                    <div class="tooltip-top_bar-item logout-container">
                                        <a href="/logout" class="button button-basic button-block whitespace-nowrap">Log out<i class="fas fa-sign-out-alt button-icon-right"></i></a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                            </div>
        </div>
    
    

    </div>

        
    
    


    
    
    
    
    <div class="strip status-page strip-item-tight">
        <h1>404: Not Found</h1>
        <img src="/images/kattis/judge.png?6dd056=" />
        <p>We&#039;re sorry, Kattis couldn&#039;t find what you were looking for.</p>
        <p>Maybe you should head back to the <a href="/">main page</a>.</p>
    </div>


    </main>

    



    <footer class="l-footer ">
        <span class="text-center text-sm">
        <a href="/info/contact">Contact</a> |
        <a href="https://status.kattis.com">System Status</a> |
        <a rel="terms-of-service" href="/info/tos">Terms of Service</a> |
        <a rel="privacy-policy" href="https://www.kattis.com/policies/privacy_policy.pdf">Privacy Policy</a>
        </span>
    </footer>

</div>



<script nonce="8684f29263b1aaa88a2c1676a856e6dee4c493b2ceb6217157e3bc6d9bd9b610" src="/assets/6ca8295fdd320959403ec48ee3c6cbbe/moment/min/moment.min.js"></script>
<script nonce="8684f29263b1aaa88a2c1676a856e6dee4c493b2ceb6217157e3bc6d9bd9b610" src="/assets/6ca8295fdd320959403ec48ee3c6cbbe/bootstrap-daterangepicker/daterangepicker.js"></script>
<script nonce="8684f29263b1aaa88a2c1676a856e6dee4c493b2ceb6217157e3bc6d9bd9b610" src="/assets/6ca8295fdd320959403ec48ee3c6cbbe/select2/dist/js/select2.full.min.js"></script>



        <script defer nonce="8684f29263b1aaa88a2c1676a856e6dee4c493b2ceb6217157e3bc6d9bd9b610" src="https://status.kattis.com/embed/script.js"></script>
</body>
</html>
