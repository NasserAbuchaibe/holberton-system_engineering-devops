# Using Puppet, create a manifest that kills a process named killmenow.

exec { 'p_kill':
  path    => '/usr/bin',
  command => 'pkill -f killmenow',
  returns => [0],
}
