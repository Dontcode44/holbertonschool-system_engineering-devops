# Pkill
exec {'killmenow':
command  => 'pkill',
provider => exec
}

