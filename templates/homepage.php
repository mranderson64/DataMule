<?php
$top = '';
$middle = '
            <div class="hero-body">
                <div class="container has-text-centered">
                    <h1 class="title">
						&#x3C;DataMule&#x3E; is a darkweb/blackmarket data visualisation tool
                    </h1>
                    <h2 class="subtitle">
						&#x3C;DataMule&#x3E; is a personal project of mine with the aim to flex/practice my skills as a developer while providing a clearnet tool for those interested in the numbers and trends without stepping foot in the darkweb
                    </h2>
                </div>
            </div>
        </section>
        <div class="box cta">
            <p class="has-text-centered">
                <span class="tag is-primary"><a href="https://liamanderson.co.uk">Alpha</a></span> &#x3C;DataMule&#x3E; is a work in progress and as such all users should expect frequent changes
            </p>
        </div>
        <section class="container">
            <div class="columns features">
                <div class="column is-4">
                    <div class="card is-shady">
                        <div class="card-image has-text-centered">
                            <i class="far fa-edit"></i>
                        </div>
                        <div class="card-content">
                            <div class="content">
                                <h4>Guest posting?</h4>
                                <p>Yes, while &lt;DataMule&gt; is the size it reports, blogs and essays will be posted through a manual process.</p>
								<p>If you wish to post on &lt;DataMule&gt; get in touch with myself via Email</p>
                                <p><a href="mailto:me@liamanderson.co.uk">Contact us</a></p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="column is-4">
                    <div class="card is-shady">
                        <div class="card-image has-text-centered">
                            <i class="fas fa-archive"></i>
                        </div>
                        <div class="card-content">
                            <div class="content">
                                <h4>Reports &amp; Essays</h4>
                                <p>&lt;DataMule&gt; will be a repository for reports and essays on the topic of dark market products and sales with accurate and up-to-date data</p>
                                <p><a href="'.$host.'/insights">Learn more</a></p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="column is-4">
                    <div class="card is-shady">
                        <div class="card-image has-text-centered">
                            <i class="fas fa-database"></i>
                        </div>
                        <div class="card-content">
                            <div class="content">
                                <h4>Data</h4>
                                <p>Can I have access to the data? "Yes, I have/will make particular Data sets available to download"</p>
								<p>Will my data collection code be made available? "Maybe, when its solid and I think its worth the eyes of the public"</p>
                                <p><a href="'.$host.'/data-cache/cache-scripts/exportDrugs.php">Download</a></p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>';
$bottom = '
			<div class="columns">
				<div id="chartContainer" style="height:370px; margin-bottom:20px;" class="column is-6 chart-50"></div>
				<div id="chartContainer1" style="height:370px; margin-bottom:20px;" class="column is-6 chart-50"></div>
			</div>
		</section>
';

$templateOutput = $top . $middle . $bottom;

$chartScripts = 'homepage-chart.php';

?>
