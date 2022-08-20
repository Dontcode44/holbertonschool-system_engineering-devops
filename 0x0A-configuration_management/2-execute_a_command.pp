# Pkill
exec {'killmenow':
command  => 'pkill -f killmenow',
provider => shell,
onlyif => '/usr/bin/ -e /usr/bin',
}

