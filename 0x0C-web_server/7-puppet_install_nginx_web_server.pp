#  Install Nginx web server (w/ Puppet) 

$nginx_config = 'server {
	listen 80 default_server;
	listen [::]:80 default_server ipv6only=on;
	root /var/www/html;
	location /redirect_me {
		return 301 https://www.holbertonschool.com/;
	}
}'

package { 'nginx install':
  ensure => latest,
  name   => 'nginx'
}

file { 'nginx site config':
  ensure  => file,
  require => Package['nginx'],
  path    => '/etc/nginx/sites-available/default',
  content => $nginx_config
}

file { 'site index':
  ensure  => file,
  require => Package['nginx'],
  path    => '/var/www/html/index.html',
  content => "Holberton School\n"
}

service { 'nginx service':
  ensure    => running,
  name      => 'nginx',
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default']
}
