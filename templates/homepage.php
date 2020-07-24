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
                            <i class="fas fa-paw"></i>
                        </div>
                        <div class="card-content">
                            <div class="content">
                                <h4>Tristique senectus et netus et. </h4>
                                <p>Purus semper eget duis at tellus at urna condimentum mattis. Non blandit massa enim nec. Integer enim neque volutpat ac tincidunt vitae semper quis. Accumsan tortor posuere ac ut consequat semper viverra nam.</p>
                                <p><a href="#">Learn more</a></p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="column is-4">
                    <div class="card is-shady">
                        <div class="card-image has-text-centered">
                            <i class="fas fa-empire"></i>
                        </div>
                        <div class="card-content">
                            <div class="content">
                                <h4>Tempor orci dapibus ultrices in.</h4>
                                <p>Ut venenatis tellus in metus vulputate. Amet consectetur adipiscing elit pellentesque. Sed arcu non odio euismod lacinia at quis risus. Faucibus turpis in eu mi bibendum neque egestas cmonsu songue. Phasellus vestibulum lorem
                                sed risus.</p>
                                <p><a href="#">Learn more</a></p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="column is-4">
                    <div class="card is-shady">
                        <div class="card-image has-text-centered">
                            <i class="fas fa-apple"></i>
                        </div>
                        <div class="card-content">
                            <div class="content">
                                <h4> Leo integer malesuada nunc vel risus. </h4>
                                <p>Imperdiet dui accumsan sit amet nulla facilisi morbi. Fusce ut placerat orci nulla pellentesque dignissim enim. Libero id faucibus nisl tincidunt eget nullam. Commodo viverra maecenas accumsan lacus vel facilisis.</p>
                                <p><a href="#">Learn more</a></p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>';
$bottom = '
			<div id="chartContainer" style="height: 370px; width: 100%;"></div>
			<div id="chartContainer1" style="height: 370px; width: 100%;"></div>
		</section>	
';

$templateOutput = $top . $middle . $bottom;

include'homepage-chart.php';
	
?>